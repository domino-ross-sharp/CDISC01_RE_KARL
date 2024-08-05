from flytekit import workflow
from flytekit.types.file import FlyteFile
from typing import TypeVar, NamedTuple
from flytekitplugins.domino.helpers import Input, Output, run_domino_job_task
from flytekitplugins.domino.task import DominoJobConfig, DominoJobTask, GitRef, EnvironmentRevisionSpecification, EnvironmentRevisionType, DatasetSnapshot


# pyflyte run --remote workflow2.py ADAMS --sdtm_data_path /mnt/imported/data/SDTMBLIND/JUNE242024
# pyflyte run --remote workflow2.py ADAMS --sdtm_data_path /mnt/data/snapshots/SDTMBLIND/1

@workflow
def ADAMS(sdtm_data_path: str):   
    # Create ADSL dataset
    adsl = run_domino_job_task(
        flyte_task_name="Create ADSL Dataset",
        command="prod/adam_flows/ADSL.sas",
        inputs=[Input(name="sdtm_data_path", type=str, value=sdtm_data_path)],
        output_specs=[Output(name="adslDataset", type=FlyteFile[TypeVar("sas7bdat")])],
        use_project_defaults_for_omitted=True,
        environment_name="SAS Analytics Pro",
        dataset_snapshots=[DatasetSnapshot(Id="66abdd45e651b51a171f2a4a", Version=1 )]
    )
    return adsl

    