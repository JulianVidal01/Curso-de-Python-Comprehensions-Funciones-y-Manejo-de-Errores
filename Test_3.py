def message_creator(text):
   match text:
      case "computadora":
         return "Con mi computadora puedo programar usando Python"
      case "celular":
         return "En mi celular puedo aprender usando la app de Platzi"
      case "cable":
         return "¡Hay un cable en mi bota!"
   return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)