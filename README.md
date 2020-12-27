# 30 days of code

## Spec
- C++
- java 11
- python 3
- Apple Swift version 5.3
- go version go1.15.2 darwin/amd64

## for C/C++

```
make Solution
./Solution.exe
```

**problem:**
- hardly to add library
- Week 7: cannot run code that hackerrate give.

```
c++     Solution.cpp   -o Solution
Solution.cpp:38:79: error: expected expression
  string::iterator new_end = unique(input_string.begin(), input_string.end(), [](const char &x, const char &y) {
                                                                              ^
1 error generated.
make: *** [Solution] Error 1
```

### How to add library

```
brew install gcc
gcc --version
cd /Library/Developer/CommandLineTools/usr/bin
cd ../include

//if bits is not created
sudo mkdir bits

sudo cp -rf <project path>/library/* /Library/Developer/CommandLineTools/usr/include/*
```

## for Java
```
javac Solution.java
java Solution
```

## for python

```
python Solution.py
```

## for swift

```
swift Solution.swift
```

## for GO
```
cd Solution_go
go run main.go
```
