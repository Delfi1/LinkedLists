#include <iterator>
#include <list>

class Iterator {
public:
    std::list<int>::iterator begin;
    std::list<int>::iterator end;
    bool finish;

    Iterator(std::list<int>::iterator begin, std::list<int>::iterator end) {
        this->begin = begin;
        this->end = end;
        this->finish = false;
    }

    bool is_finished() {
        return this->begin == this->end;
    }

    int get() {
        return *this->begin;
    }

    void next() {
        this->begin++;
    }
};

extern "C"
{
    __declspec(dllexport) std::list<int>* init() { return new std::list<int>(); }
    __declspec(dllexport) void insert(std::list<int> *self, int index, int value) {
        auto it = self->begin();
        std::advance(it, index);
        self->insert(it, value);
    }
    __declspec(dllexport) void pushHead(std::list<int> *self, int value) { self->push_front(value); }
    __declspec(dllexport) void pushBack(std::list<int> *self, int value) { self->push_back(value); }

    __declspec(dllexport) void popHead(std::list<int> *self) { self->pop_front(); }
    __declspec(dllexport) void popBack(std::list<int> *self) { self->pop_back(); }
    __declspec(dllexport) void pop(std::list<int> *self, int index) {
        auto it = self->begin();
        std::advance(it, index);
        self->erase(it);
    }

    __declspec(dllexport) int lenght(std::list<int> *self) { return self->size(); }

    __declspec(dllexport) Iterator* iter(std::list<int> *self) { return new Iterator(self->begin(), self->end()); }
    __declspec(dllexport) void next(Iterator *self) { return self->next(); }
    __declspec(dllexport) bool is_finished(Iterator *self) { return self->is_finished(); }
    __declspec(dllexport) int get(Iterator *self) { return self->get(); }
}
