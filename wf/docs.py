from latch.types.metadata import (
    LatchAuthor,
    LatchMetadata,
    LatchParameter,
    Params,
    Section,
    Text,
)

PARAMS = {
    "samplesheet": LatchParameter(
        display_name="Input samplesheet",
    ),
    "out": LatchParameter(display_name="Output directory"),
}

FLOW = [
    Section(
        "Samples",
        Text(
            "The samplesheet must be a list of identifiers, one on each line."
            "Currently accepted run identifiers are SRA, ERA and DDBJ IDs."
        ),
        Params("samplesheet"),
    ),
    Section("Output", Text("The name of the output directory."), Params("out")),
]

WORKFLOW_NAME = "nfcore_fetchngs"

wf_docs = LatchMetadata(
    display_name="nf-core/fetchngs",
    documentation=f"https://github.com/jvfe/{WORKFLOW_NAME}_latch/blob/main/README.md",
    author=LatchAuthor(
        name="jvfe",
        github="https://github.com/jvfe",
    ),
    repository=f"https://github.com/jvfe/{WORKFLOW_NAME}_latch",
    license="MIT",
    parameters=PARAMS,
    tags=["NGS"],
    flow=FLOW,
)
