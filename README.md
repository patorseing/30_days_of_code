# 30 days of code

## Spec

* [C++](##-for-C/C++)
* [java 11](##-for-Java)
* [python 3](##-for-Python)
* [Apple Swift version 5.3](##-for-Swift)
* [go version go1.15.2 darwin/amd64](##-for-Go)

## for C/C++

[<< Back](##-Spec)

```bash
cd Solution_cpp/main
make Solution
mv Solution Solution.exe
./Solution.exe
```

### (C/C++) for test

```bash
cd Solution_cpp/main
bazel test solution-test
```

**problem:**

* hardly to add library
* Week 7: cannot run code that hackerrate give.

```bash
c++     Solution.cpp   -o Solution
Solution.cpp:38:79: error: expected expression
  string::iterator new_end = unique(input_string.begin(), input_string.end(), [](const char &x, const char &y) {
                                                                              ^
1 error generated.
make: *** [Solution] Error 1
```

### How to add library

```bash
brew install gcc
gcc --version
cd /Library/Developer/CommandLineTools/usr/bin
cd ../include

//if bits is not created
sudo mkdir bits

sudo cp -rf <project path>/library/* /Library/Developer/CommandLineTools/usr/include/*
```

## for Java

[<< Back](##-Spec)

```bash
javac Solution.java
java Solution
```

## for python

[<< Back](##-Spec)

```bash
python Solution.py
```

## for swift

[<< Back](##-Spec)

```bash
swift Solution.swift
```

## for GO

[<< Back](##-Spec)

```bash
cd Solution_go
go run main.go
```
