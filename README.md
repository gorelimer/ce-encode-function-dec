# Cheat Engine function decoder and decompiler
## Installing
works only on windows

install python3

clone this repo or download zip
## Usage
for example we have a function
```lua
function foo()
    return nil
end
```
after encoding the function via encodeFunction we get the string
```
c-oWpDNPJ!ketlRCB=/U!NS2(5ypT38s!cQ42)bqGnmT,qF8]f4JfL^)7:ET002?01s=
```
run mine.py and enter the coded function
```
python main.py
```
also you can add add path to text file containing function
```
python main.py <filepath>
```
after execution, an output folder will be created in the program folder, which will contain two files:
- decoded.luac - decoded lua bytecoded
- decompiled - decompiled lua code

decompiled code for our example
```
-- Decompiled using luadec 2.2 rev: a18776c for Lua 5.3 from https://github.com/zhangjiequan/luadec
-- Command line: output\decoded.luac 

-- params : 
-- function num : 0
return nil
```


thanks @zhangjiequan for lua5.3 decompiler 

thanks @FeeeeK for function decoder
