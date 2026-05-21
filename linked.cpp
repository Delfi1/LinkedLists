#include <cstdio>
#include <cstdlib>
#include <malloc.h>

class Node {
public:
  int data;

  Node* prev;
  Node* next;

  Node(int value) {
      data = value;
      prev = nullptr;
      next = nullptr;
  }
};

class LinkedList {
public:
    Node* head;
    Node* back;
    Node* empty;
    int len;

    LinkedList() {
        head = nullptr;
        back = nullptr;
        this->getMem();
        len = 0;
    }

    void insert(int index, int value) {
        if (index < 0 || index > len) {
            printf("Index is out of range 0..%d\n", len);
            return;
        }

        if (len == 0) {
            this->init(value);
            return;
        }

        if (index == 0) {
            this->pushHead(value);
            return;
        }

        if (index == len) {
            this->pushBack(value);
            return;
        }

        Node* node = head;
        for (int j = 1; j < index; j++) {
            node = node->next;
        }

        empty->data = value;
        empty->next = node->next;
        empty->prev = node;
        if (node->next != nullptr) node->next->prev = empty;
        node->next = empty;

        this->getMem();
        len++;
        return;
    }

    void pushHead(int value) {
        if (len == 0) {
            this->init(value);
            return;
        }

        empty->data = value;
        empty->next = head;
        head->prev = empty;
        head = empty;

        this->getMem();
        len++;
        return;
    }

    void pushBack(int value) {
        if (len == 0) {
            this->init(value);
            return;
        }

        empty->data = value;
        back->next = empty;
        empty->prev = back;
        back = empty;

        this->getMem();
        len++;
        return;
    }

    void popHead() {
        if (len == 0) return;

        if (len == 1) {
            head = nullptr;
            back = nullptr;
            return;
        }

        head = head->next;
        len--;
    }

    void popBack() {
        if (len == 0) return;

        if (len == 1) {
            head = nullptr;
            back = nullptr;
            return;
        }

        back = back->prev;
        len--;
    }

    void pop(int index) {
        if (index < 0 || index >= len) {
            printf("Index is out of range 0..%d\n", len - 1);
            return;
        }

        if (len == 0) return;

        if (index == 0) {
            this->popHead();
            return;
        }

        if (index == len-1) {
            this->popBack();
            return;
        }

        Node* node = head;
        for (int j = 1; j <= index; j++) {
            node = node->next;
        }

        node->prev->next = node->next;
        node->next->prev = node->prev;

        len--;
    }

    int get(int index) {
        if (index < 0 || index >= len) {
            printf("Index is out of range 0..%d\n", len - 1);
            return 0;
        }

        Node* node = this->head;
        for (int j=1; j <= index; j++) {
            node = node->next;
        }

        return node->data;
    }

    int lenght() {
        return this->len;
    }

    void print() {
        if (len == 0) return;

        Node* node = head;
        printf("%d", node->data);
        for (int j=1; j < len; j++) {
            node = node->next;
            printf(" <-> %d", node->data);
        }
        printf("\n");
    }

private:
    void init(int value) {
        head = empty;
        head->data = value;
        head->next = nullptr;
        head->prev = nullptr;
        back = head;

        this->getMem();
        len++;
        return;
    }

    void getMem() {
        empty = (Node*)malloc(sizeof(Node));
        empty->data = 0;
        empty->next = nullptr;
        empty->prev = nullptr;
    }
};

int main() {
    LinkedList list = LinkedList();
    list.insert(0, 10);
    list.print();

    list.insert(0, 20);
    list.print();

    list.insert(0, 30);
    list.print();

    list.insert(1, 40);
    list.print();

    list.pop(0);
    list.print();

    list.pop(1);
    list.print();

    list.pop(1);
    list.print();

    return 0;
}

extern "C"
{
    __declspec(dllexport) LinkedList* init() { return new LinkedList(); }
    __declspec(dllexport) void insert(LinkedList *self, int index, int value) { self->insert(index, value); }
    __declspec(dllexport) void pushHead(LinkedList *self, int value) { self->pushHead(value); }
    __declspec(dllexport) void pushBack(LinkedList *self, int value) { self->pushBack(value); }

    __declspec(dllexport) void popHead(LinkedList *self) { self->popHead(); }
    __declspec(dllexport) void popBack(LinkedList *self) { self->popBack(); }
    __declspec(dllexport) void pop(LinkedList *self, int index) { self->pop(index); }

    __declspec(dllexport) int lenght(LinkedList *self) { return self->lenght(); }
    __declspec(dllexport) int get(LinkedList *self, int index) { return self->get(index); }
}
