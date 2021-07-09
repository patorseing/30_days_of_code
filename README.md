# 30 days of code

[https://www.hackerrank.com/domains/tutorials/30-days-of-code?filters%5Bstatus%5D%5B%5D=unsolved&filters%5Bstatus%5D%5B%5D=solved&filters%5Bsubdomains%5D%5B%5D=30-days-of-code&badge_type=30-days-of-code](https://www.hackerrank.com/domains/tutorials/30-days-of-code?filters%5Bstatus%5D%5B%5D=unsolved&filters%5Bstatus%5D%5B%5D=solved&filters%5Bsubdomains%5D%5B%5D=30-days-of-code&badge_type=30-days-of-code)

## Spec

* [C++](##-for-C/C++)
* [java 11](##-for-Java)
* [python 3](##-for-Python)
* [javascript v10.15.3](##-for-Javascript-(node.js))
* [Apple Swift version 5.3](##-for-Swift)
* [go version go1.15.2 darwin/amd64](##-for-Go)
* [Rust](##-for-Rust)

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
bazel run //main:solution
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

### How to add library (C++)

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
junit Solution // for unit test
java Solution
```

### How to add library (java)

```bash
//download
//Ex junit: https://github.com/junit-team/junit4/wiki/Download-and-Install
cp ~/Download/*.jar /Library/Java/Extensions/
```

#### if you not setup zsh

```zsh
//zsh
export JUNIT_HOME=/Library/Java/Extensions
export PATH=$PATH:$JUNIT_HOME
export CLASSPATH=$CLASSPATH:$JUNIT_HOME/junit-4.13.2.jar:$JUNIT_HOME/hamcrest-core-1.3.jar
alias junit="java org.junit.runner.JUnitCore"
```

## for python

[<< Back](##-Spec)

```bash
cd Solution_py
python -m unittest
python Solution.py
```

## for Javascript (node.js)

[<< Back](##-Spec)

```bash
mkdir Solution_node
cd Solution_node
npm init -y
code index.js
npm start
```

## for swift

[<< Back](##-Spec)

```bash
swift Solution.swift
```

** run with xcode\
tutorial
<https://youtu.be/TSbzwqGzYC0>

## for GO

[<< Back](##-Spec)

```bash
cd Solution_go
go test
go test <case>
go test -cover -v
go test -cover -v -covermode=count -coverprofile=count.out fmt
go run main.go
```

## for Rust

[<< Back](##-Spec)

```bash
cargo new Solution_rust
cd Solution_rust

cargo build
./target/debug/Solution_rust

cargo run

cargo check

cargo test
```

<https://learning-rust.github.io/docs/a1.why_rust.html>
