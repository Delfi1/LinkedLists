program Integrals;
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
  i, j, v, len: integer;
  key: char;
  m, head, back: PNode;

const
  SIZE: integer = 1024;
  N: integer = 7;
  list: array[0..6] of string = ('Push back', 'Pop back', 'Push front', 'Pop front', 'Count', 'Print', 'Exit');

procedure pushBack;
var new: PNode;
begin
  ClrScr;

  write('Value: ');
  readln(v);

  if back = nil then begin
    head^.value := v;
    head^.next := nil;
    head^.prev := nil;

    new := head;
  end else begin
    new := back + 1;
    new^.value := v;
    new^.next := nil;
    new^.prev := back;

    back^.next := new;
  end;

  back := new;
  inc(len);
end;

procedure popBack;
begin
  ClrScr;

  if back = nil then exit;

  if head <> back then begin
    back := back^.prev;
    back^.next := nil;
  end else back := nil;

  dec(len);
end;

procedure pushFront;
var new: PNode;
begin
  ClrScr;

  write('Value: ');
  readln(v);

  if back = nil then begin
    head^.value := v;
    head^.next := nil;
    head^.prev := nil;

    new := head;
  end else begin
    new := head - 1;
    new^.value := v;
    new^.next := head;
    new^.prev := nil;

    head^.prev := new;
  end;

  head := new;
  inc(len);
end;

procedure popFront;
begin
  ClrScr;

  if back = nil then exit;

  if head <> back then begin
    head := head^.next;
    head^.prev := nil;
  end else back := nil;

  dec(len);
end;

procedure printValues;
var point: PNode;
begin
  ClrScr;

  if back = nil then exit;

  writeln('Values: ');
  if head = back then begin
    write(head^.value);
    exit;
  end;

  write(head^.value);
  point := head;
  j := 1;
  while point^.next <> nil do begin
    point := head + j;
    write(' <-> ', point^.value);
    j += 1;
  end;

end;

begin
  ClrScr;

  run := 1;
  GetMem(m, SIZE);
  head := m + SIZE div 2;
  back := nil;

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
          0: pushBack;
          1: popBack;
          2: pushFront;
          3: popFront;
          4: begin
            writeln('Queue lenght: ', len);
            ReadKey;
          end;
          5: begin
            printValues;
            if len <> 0 then ReadKey;
          end;
          6: run := 0;
        end;
      end;
    end;

    current := (current + N) mod N;
  end;

end.
