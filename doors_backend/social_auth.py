# -*- coding: utf-8 -*-


# Модель пользователя. Здесь стандартная.
SOCIAL_AUTH_USER_MODEL = 'auth.User'


AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Проверка url перенаправления
SOCIAL_AUTH_SANITIZE_REDIRECTS = True

# FACEBOOK
# Только для facebook, указываем запрашиваемые поля
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id, name, email',
}
# Разрешение на получение поля email
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

# Ключи
SOCIAL_AUTH_FACEBOOK_KEY = 'facebook-app-id'
SOCIAL_AUTH_FACEBOOK_SECRET = 'facebook-app-key'

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '761611068364-4j31b12eq7t5301b2bhkkf7v6f81lmk5.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'oDMzaZikoB7SQNQk4XVorm5g'