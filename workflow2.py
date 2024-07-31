import os
from flytekit import workflow
from flytekitplugins.domino.task import DominoJobConfig, DominoJobTask


# pyflyte run --remote workflow2.py POC_HW --sdtm_data_path /mnt/imported/data/SDTMBLIND/JUNE242024

@workflow
def POC_HW(sdtm_data_path: str):   
    # Create ADSL dataset
    data_prep_results = run_domino_job_task(
        flyte_task_name="ADSL Dataset",
        command="prod/adam_flows/ADSL.sas",
        inputs=[Input(name="sdtm_data_path", type=str, value=sdtm_data_path)],
        output_spec=[Output(name="ADSL Dataset", type=FlyteFile[TypeVar("sas7bdat")])],
        use_project_defaults_for_omitted=True,
        environment_name="SAS Analytics Pro",
        dataset_snapshot=[DatasetSnapshot(Id="6679f7650d33391416fd83bc", Version=1)]
    )