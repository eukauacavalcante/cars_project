from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'model': forms.TextInput(attrs={
                'class': 'input-global',
            }),
            'brand': forms.Select(attrs={
                'class': 'input-global',
            }),
            'plate': forms.TextInput(attrs={
                'class': 'input-global',
            }),
            'color': forms.TextInput(attrs={
                'class': 'input-global',
            }),
            'value': forms.NumberInput(attrs={ 
                'class': 'input-global',
                'step': '0.01',
                'min': '0',
            }),
            'factory_year': forms.NumberInput(attrs={
                'class': 'input-global',
                'min': '1975',
            }),
            'model_year': forms.NumberInput(attrs={
                'class': 'input-global',
                'min': '1975',
            }),
            'description': forms.Textarea(attrs={
                'class': 'input-global w-full resize-none',
                'rows': '3',
            }),
            'photo': forms.FileInput(attrs={
                'class': 'input-global input-photo',
                'accept': 'image/jpeg,image/png,image/jpg,image/webp',
            }),
        }

    def clean_model(self):
        model = self.cleaned_data.get('model')
        return model.title()

    def clean_value(self):
        value = self.cleaned_data.get('value')

        if value is None:
            raise ValidationError('O valor é obrigatório')

        if value < 20000:
            raise ValidationError('O valor mínimo é de R$ 20.000,00')

        if value > 10000000:  # 10 milhões
            raise ValidationError('O valor máximo é de R$ 10.000.000,00')

        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        current_year = datetime.now().year

        if factory_year < 1975:
            raise ValidationError('Não aceitamos veículos fabricados antes de 1975')

        if factory_year > current_year:
            raise ValidationError(f'O ano de fabricação não pode ser maior que {current_year}')

        return factory_year

    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        current_year = datetime.now().year

        if model_year < 1975:
            raise ValidationError('Não aceitamos veículos com ano de modelo anterior a 1975')

        if model_year > current_year + 1:
            raise ValidationError(f'O ano do modelo não pode ser maior que {current_year + 1}')

        return model_year

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')

        if photo:
            valid_extensions = ['jpg', 'jpeg', 'png', 'webp']
            ext = photo.name.split('.')[-1].lower()

            if ext not in valid_extensions:
                raise ValidationError('Apenas arquivos JPG, JPEG, PNG e WEBP são permitidos')

            # Validar tamanho (máximo 5MB)
            if photo.size > 5 * 1024 * 1024:
                raise ValidationError('A imagem deve ter no máximo 5MB')

        return photo

    def clean_color(self):
        color = self.cleaned_data.get('color')

        if color.isdecimal():
            raise ValidationError('Insira apenas letras')
        
        return color.title()

    def clean(self):
        cleaned_data = super().clean()
        factory_year = cleaned_data.get('factory_year')
        model_year = cleaned_data.get('model_year')

        if factory_year and model_year:
            if model_year < factory_year:
                raise ValidationError({
                    'model_year': 'O ano do modelo não pode ser menor que o ano de fabricação'
                })

            if model_year > factory_year + 1:
                raise ValidationError({
                    'model_year': 'O ano do modelo pode ser no máximo 1 ano maior que o ano de fabricação'
                })

        return cleaned_data
