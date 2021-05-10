from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import MinimumLengthValidator, UserAttributeSimilarityValidator, CommonPasswordValidator, NumericPasswordValidator
from django.core.exceptions import ValidationError
import re
from difflib import SequenceMatcher

from django.utils.translation import ngettext

class MinimumLengthValidatorCustom(MinimumLengthValidator):
	def validate(self, password, user=None):
		if len(password) < self.min_length:
			raise ValidationError(
				ngettext(
					"Пароль слишком короткий. Он должен содержать не менее %(min_length)d символов.",
					"Пароль слишком короткий. Он должен содержать минимум %(min_length)d символов.",
					self.min_length
				),
				code='password_too_short',
				params={'min_length': self.min_length},
			)

	def get_help_text(self):
		return ngettext(
			"Ваш пароль должен содержать не менее %(min_length)d символов.",
			"Ваш пароль должен содержать не менее %(min_length)d символов.",
			self.min_length
		) % {'min_length': self.min_length}

class UserAttributeSimilarityValidatorCustom(UserAttributeSimilarityValidator):
	def validate(self, password, user=None):
		if not user:
			return

		for attribute_name in self.user_attributes:
			value = getattr(user, attribute_name, None)
			if not value or not isinstance(value, str):
				continue
			value_parts = re.split(r'\W+', value) + [value]
			for value_part in value_parts:
				if SequenceMatcher(a=password.lower(), b=value_part.lower()).quick_ratio() >= self.max_similarity:
					try:
						verbose_name = str(user._meta.get_field(attribute_name).verbose_name)
					except FieldDoesNotExist:
						verbose_name = attribute_name
					raise ValidationError(
						("Пароль слишком похож на %(verbose_name)s."),
						code='password_too_similar',
						params={'verbose_name': verbose_name},
					)

	def get_help_text(self):
		return ("В целях безопасности Ваш пароль не может быть слишком похож на Ваш логин. Придумайте новый пароль.")

class CommonPasswordValidatorCustom(CommonPasswordValidator):
	def validate(self, password, user=None):
		if password.lower().strip() in self.passwords:
			raise ValidationError(
				("Пароль слишком прост для взлома. Пример сложного пароля – Q1234werty"),
				code='password_too_common',
			)

	def get_help_text(self):
		return ("Этот пароль слишком прост для взлома. Придумайте новый пароль.")

class NumericPasswordValidatorCustom(NumericPasswordValidator):
	def validate(self, password, user=None):
		if password.isdigit():
			raise ValidationError(
				("Пароль полностью состоит из цифр."),
				code='password_entirely_numeric',
			)

	def get_help_text(self):
		return ("Ваш пароль не может состоять только из цифр. Придумайте новый пароль.")