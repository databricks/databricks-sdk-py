from databricks.sdk.core import (ApiClient, Config, CredentialsProvider,
                                 credentials_strategy)
from databricks.sdk.service.iam import CurrentUserAPI


@credentials_strategy("custom", ["host"])
def user_input_token(cfg: Config) -> CredentialsProvider:
    pat = input("Enter Databricks PAT: ")

    def inner() -> dict[str, str]:
        return {"Authorization": f"Bearer {pat}"}

    return inner


if __name__ == "__main__":
    host = input("Enter Databricks host: ")

    cfg = Config(host=host, credentials_provider=user_input_token)

    api_client = ApiClient(cfg)
    current_user = CurrentUserAPI(api_client)
    me = current_user.me()

    print(f"Current user is: {me.user_name}")
