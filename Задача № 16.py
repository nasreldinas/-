#КОД ПРИМЕРА «Работа с двумерными массивами (матрицами)»
#номер версии: 1.0
#имя файла: Задача № 16.py
#автор и его учебная группа: A. nasreldin, ЭУ-135
#дата создания: 18.06.2021
#дата последней модификации: 18.06.2021
#описание: Ветвления и оператор выбора
#версия Python:3.9.2


const N = 3; M = 4;
var 
    mtx: array[1..N,1..M] of byte;
    arr: array[1..N*M] of byte;
    i,j,k: byte;
begin
    randomize;
    for i:=1 to N do begin
        for j:=1 to M do begin
            mtx[i,j] := random(100);
            write(mtx[i,j]:3);
        end;
        writeln;
    end;
    writeln;
 
    k := 0;
    for j:=1 to M do
        for i:=1 to N do begin
            k := k + 1;
            arr[k] := mtx[i,j];
            write(arr[k]:3);
        end;
    writeln;
end.
