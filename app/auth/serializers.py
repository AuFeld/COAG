from app.auth.models import Token
from app.serializers.common import ModelSerializer


class TokenSerializer(ModelSerializer):
    """
    Serializer for the default `Token` model.
    Use it if you use default model.
    """

    class Meta:
        model = Token
        exclude = {"user_id"}
