from core.filters import ItemFilter, FuncionalidadFilter, ItemsPadreFilter
from rest_framework.response import Response
from rest_framework import status

__author__ = 'LFL'

from django.contrib.auth.models import Group, User, Permission

from rest_framework import serializers, viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



from .models import Catalogo, Item, Parametro, Modulo, Funcionalidad

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission

class PermissionViewSet(viewsets.ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()


class CatalogoPadreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = ('id', 'nombre', 'codigo', 'descripcion', 'estado', 'padre', 'editable')


class CatalogoSerializer(serializers.ModelSerializer):
    #padre = CatalogoPadreSerializer()
    padreCodigo = serializers.SerializerMethodField('get_padre_codigo')

    class Meta:
        model = Catalogo
        fields = ('id', 'nombre', 'codigo', 'descripcion', 'estado', 'padre', 'padreCodigo', 'editable',)
        extra_kwargs = {'padre': {'prueba': 'nombre'}}
        #read_only_fields = ('codigo',)

    def get_padre_codigo(self, obj):

        if obj.padre is None:
            return None
        else:
            return obj.padre.codigo

    # def validate_nombre(self, value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return value



class CatalogoViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogoSerializer
    queryset = Catalogo.objects.all().order_by('nombre')
    ordering = ('nombre', 'codigo')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        #fields = ['id', 'oferente', 'intencion', 'ofrenda', 'fecha', 'hora', 'parroquia', 'iglesia', 'individual']


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all().order_by('nombre')
    filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ('codigo',)
    #filter_class = ItemFilter
    filter_class = ItemsPadreFilter


    def get_queryset(self):
        query = self.request.QUERY_PARAMS
        print query
        if 'catalogo' in query.keys():
            return self.queryset
        else:
            #return self.queryset.none()
            return self.queryset

    # def list(self, request):
    #     if self.queryset is None:
    #         return Response({"as":"ew"}, status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         queryset = Item.objects.all()
    #         serializer = ItemSerializer(queryset, many=True)
    #         return Response(serializer.data)


class ParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametro

class ParametroViewSet(viewsets.ModelViewSet):
    serializer_class = ParametroSerializer
    queryset = Parametro.objects.all()


class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo

class ModuloViewSet(viewsets.ModelViewSet):
    serializer_class = ModuloSerializer
    queryset = Modulo.objects.all()

class FuncionalidadSerializer(serializers.ModelSerializer):
    grupos_usuario = GroupSerializer(many=True)
    class Meta:
        model = Funcionalidad
        fields = ('id', 'nombre','url','codigo','modulo','estado','descripcion','orden','icono','grupos_usuario')

class FuncionalidadViewSet(viewsets.ModelViewSet):
    serializer_class = FuncionalidadSerializer
    queryset = Funcionalidad.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = FuncionalidadFilter




