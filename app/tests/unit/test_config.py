def test_environment(app):
    assert app.config["ENV_STATUS"] == "On Testing"
    assert app.config.current_env == "testing"


def test_dynaconf_settings_is_the_same_object(app):
    from dynaconf import settings

    assert settings is app.config._settings
    assert app.config["ENV_STATUS"] == settings.ENV_STATUS
    assert app.config.current_env == settings.current_env
