from maltego_trx.decorator_registry import TransformSetting

api_key_setting = TransformSetting(
    name="telegram_session", display_name="Telegram session", setting_type="string", global_setting=False
)

language_setting = TransformSetting(
    name="language",
    display_name="Language",
    setting_type="string",
    default_value="en",
    optional=True,
    popup=True,
)
