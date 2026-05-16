program LinkedLists;
uses Crt;

type
  PNode = ^TNode;
  TNode = record
    value: integer;
    next: PNode;
    prev: PNode;
  end;

var
  current, run: integer;
  i, j, k, v, len: integer;
  key: char;
  empty, head, back: PNode;

const
  N: integer = 5;
  list: array[0..4] of string = ('Push', 'Pop', 'Count', 'Print', 'Exit');

procedure push;
var new, index: PNode;
begin
  ClrScr;

  write('Value: ');
  readln(v);

  if head = nil then begin
    head := empty;
    head^.value := v;
    head^.next := nil;
    head^.prev := nil;
    back := head;
  end else begin
    write('Index: ');
    readln(k);

    if (k < 0) or (k > len) then begin
      writeln('Index is out of range 0..', len);
      ReadKey;
      Exit;
    end;

    new := empty;
    new^.value := v;
    new^.prev := nil;
    new^.next := nil;

    if k = 0 then begin
      new^.next := head;
      head^.prev := new;
      head := new;
    end else if k = len then begin
      back^.next := new;
      new^.prev := back;
      back := new;
    end else begin
      index := head;
      for j := 0 to k-2 do begin
        index := index^.next;
      end;

      new^.next := index^.next;
      new^.prev := index;
      if index^.next <> nil then index^.next^.prev := new;
      index^.next := new;
    end;
  end;

  GetMem(empty, 1);
  inc(len);
end;

procedure pop;
var index: PNode;
begin
  ClrScr;

  if head = nil then exit;

  if len = 1 then head := nil
  else begin
    write('Index: ');
    readln(k);

    if (k < 0) or (k >= len) then begin
      writeln('Index is out of range 0..', len);
      ReadKey;
      Exit;
    end;

    if k = 0 then begin
      head := head^.next;
      head^.prev := nil;
    end else if k = len - 1 then begin
      back := back^.prev;
      head^.next := nil;
    end else begin
      index := head;
      for j := 0 to k-1 do begin
        index := index^.next;
      end;

      index^.prev^.next := index^.next;
      index^.next^.prev := index^.prev;
    end;
  end;

  dec(len);
end;

procedure printValues;
var point: PNode;
begin
  ClrScr;

  if head = nil then exit;

  writeln('Values: ');
  if len = 1 then begin
    write(head^.value);
    exit;
  end;

  write(head^.value);
  point := head;
  while point^.next <> nil do begin
    point := point^.next;
    write(' <-> ', point^.value);
  end;

end;

begin
  ClrScr;

  run := 1;
  GetMem(empty, 1);
  head := nil;

  current := 0;
  while run <> 0 do begin
    ClrScr;

    for i := 0 to N-1 do begin
      if i = current then write('--> ');
      writeln(list[i]);
    end;
    key := ReadKey;

    case key of
      #72: current -= 1;
      #80: current += 1;
      #13: begin
        writeln();

        case current of
          0: push;
          1: pop;
          2: begin
            writeln('Queue lenght: ', len);
            ReadKey;
          end;
          3: begin
            printValues;
            if len <> 0 then ReadKey;
          end;
          4: run := 0;
        end;
      end;
    end;

    current := (current + N) mod N;
  end;

end.
