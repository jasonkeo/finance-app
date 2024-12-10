from openai import OpenAI
client = OpenAI(api_key="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")

msg = "What is the capital of the United States?"
completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": msg
                    }
                ]
            )

res = completion.choices[0].message.content
print(res)