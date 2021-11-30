def beCheerful(name='', repeat=2):		# asignar defaults cuando se declare los parámetros
	print(f"good morning {name}\n" * repeat)
beCheerful()				# salida: good morning (repeated on 2 lines)
beCheerful("tim")		        # salida: good morning tim (repeated on 2 lines)
beCheerful(name="john")			# salida: good morning john (repeated on 2 lines)
beCheerful(repeat=6)			# salida: good morning (repeated on 6 lines)
beCheerful(name="michael", repeat=5)	# salida: good morning michael (repeated on 5 lines)
# NOTA: el orden de loa argumentos no importa si estamos implícitos al enviar nuestros argumentos!
beCheerful(repeat=3, name="kb")		# salida: good morning kb (repeated on 3 lines)