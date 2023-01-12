import subprocess
from pathlib import Path

from latch import medium_task, workflow
from latch.resources.launch_plan import LaunchPlan
from latch.types import LatchDir, LatchFile

from .docs import wf_docs


@medium_task(retries=10)
def fetchngs_task(samplesheet: LatchFile, out: str) -> LatchDir:

    results_dir = Path("methylseq_results").resolve()

    methylseq_cmd = [
        f"""
        nextflow run nf-core/fetchngs \
        -profile conda \
        -r 1.9 \
        --input {samplesheet.local_path} \
        --outdir {str(results_dir)}
        """
    ]

    subprocess.run(methylseq_cmd, check=True, shell=True)

    return LatchDir(str(results_dir), f"latch:///{out}")


@workflow(wf_docs)
def fetchngs(
    samplesheet: LatchFile,
    out: str = "fetchngs_results",
) -> LatchDir:
    """Pipeline to fetch metadata and raw FastQ files from public and private databases

    nf-core/fetchngs
    ------

    nf-core/fetchngs is a bioinformatics pipeline to fetch metadata and raw FastQ files from both public and private databases. At present, the pipeline supports SRA / ENA / DDBJ / Synapse ids.

    ## Citations

    If you use nf-core/fetchngs for your analysis, please cite it using the following doi: 10.5281/zenodo.5070524

    """
    return fetchngs_task(samplesheet=samplesheet, out=out)


LaunchPlan(
    fetchngs,
    "Test Data",
    {
        "samplesheet": LatchFile(
            "s3://latch-public/test-data/4318/fetchngs_sra_ids_test.csv"
        ),
        "out": "fetchngs_results",
    },
)
