import resend

resend.api_key = "re_SAfEKnuF_Kb1vyhXUV2ramqupbxLgkE9e"

r = resend.Emails.send({
  "from": "onboarding@resend.dev",
  "to": "livianascimento626@gmail.com",
  "subject": "Vem pra faculdade amorrrrrr",
  "html": "<p>Esse é um email usando api  <strong>meu primeiro email</strong>!</p>"
})