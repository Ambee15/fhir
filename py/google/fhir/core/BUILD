load("@fhir_bazel_pip_dependencies//:requirements.bzl", "requirement")

# Placeholder for internal Python strict contrib test and library compatibility macro.

package(default_visibility = [
    "//visibility:public",
])

licenses(["notice"])

py_library(
    name = "codes",
    srcs = [
        "codes.py",
    ],
    srcs_version = "PY3",
    deps = [
        ":fhir_errors",
        "//proto/google/fhir/proto:annotations_py_pb2",
        "//py",
        "//py/google/fhir/core/utils:annotation_utils",
        "//py/google/fhir/core/utils:fhir_types",
        "//py/google/fhir/core/utils:proto_utils",
        "@com_google_protobuf//:protobuf_python",
    ],
)

py_library(
    name = "fhir_errors",
    srcs = [
        "fhir_errors.py",
    ],
    srcs_version = "PY3",
    deps = ["//py"],
)

py_test(
    name = "fhir_errors_test",
    srcs = ["fhir_errors_test.py"],
    legacy_create_init = 0,
    python_version = "PY3",
    srcs_version = "PY3",
    deps = [
        ":fhir_errors",
        "//py",
        requirement("absl-py"),
        requirement("six"),
    ],
)

py_library(
    name = "extensions",
    srcs = [
        ":extensions.py",
    ],
    srcs_version = "PY3",
    deps = [
        ":codes",
        ":fhir_errors",
        "//proto/google/fhir/proto:annotations_py_pb2",
        "//py",
        "//py/google/fhir/core/utils:annotation_utils",
        "//py/google/fhir/core/utils:fhir_types",
        "//py/google/fhir/core/utils:proto_utils",
        "@com_google_protobuf//:protobuf_python",
    ],
)

py_library(
    name = "extensions_test",
    testonly = 1,
    srcs = [
        ":extensions_test.py",
    ],
    srcs_version = "PY3",
    deps = [
        ":extensions",
        "//py",
        "//py/google/fhir/core/testing:testdata_utils",
        "@com_google_protobuf//:protobuf_python",
        requirement("absl-py"),
        requirement("six"),
    ],
)

py_library(
    name = "references",
    srcs = [
        ":references.py",
    ],
    srcs_version = "PY3",
    deps = [
        "//py",
        "//py/google/fhir/core/utils:annotation_utils",
        "//py/google/fhir/core/utils:path_utils",
        "//py/google/fhir/core/utils:proto_utils",
        "@com_google_protobuf//:protobuf_python",
    ],
)
