import os
import sys

from pathlib import Path
from pprint import pprint

from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthClientCredentials

# This is necessary to import adjacent modules in the function code.
sys.path.insert(0, str(Path(__file__).parent / "local_code"))

from local_code.handler import handle # noqa: E402


def main() -> None:
    credentials = OAuthClientCredentials(
        token_url="https://login.microsoftonline.com/16e3985b-ebe8-4e24-9da4-933e21a9fc81/oauth2/v2.0/token",
        client_id="0fabc792-6a92-47e3-9d10-a1b4adfe6336",
        client_secret=os.environ["DATA_PIPELINE_OEE_CLIENT_SECRET"],
        scopes=['https://westeurope-1.cognitedata.com/.default'],
    )

    client = CogniteClient(
        config=ClientConfig(
            client_name="CDF-Toolkit:0.5.30",
            project="cdf-bootcamp-06-test",
            base_url="https://westeurope-1.cognitedata.com",
            credentials=credentials,
        )
    )

    print("oee_timeseries LOGS:")
    response = handle(
        client=client,
        data={},
    )

    print("oee_timeseries RESPONSE:")
    pprint(response)


if __name__ == "__main__":
    main()
