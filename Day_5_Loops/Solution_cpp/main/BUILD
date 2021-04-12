# https://docs.bazel.build/versions/master/be/c-cpp.html#cc_library
cc_library(
  name = "solution_lib",
  hdrs = ["bits/stdc++.h", "Solution.hpp"],
)
# https://docs.bazel.build/versions/master/be/c-cpp.html#cc_binary
cc_binary(
  name = "solution",
  srcs = ["Solution.cpp"],
  deps = [":solution_lib"],
)

cc_test(
  name = "solution-test",
  srcs = ["Solution_test.cpp"],
  deps = [
    ":solution_lib",
    "@gtest//:gtest",
    "@gtest//:gtest_main" # Only if hello_test.cc has no main()
  ],
)
