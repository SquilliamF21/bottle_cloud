py_binary(
    name = "main",
    srcs = ["main.py"],
    data = [":transform"],  # a cc_binary which we invoke at run time
    deps = [
        "flask"
    ]
)