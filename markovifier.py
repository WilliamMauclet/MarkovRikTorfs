import markovify

# Get raw text as string.
with open("./torfsrik_tweets.csv") as f:
    text = f.read()
# Build the model.
text_model = markovify.NewlineText(text, state_size=3)

# Print five randomly-generated sentences
# for k, i in enumerate([key for key in text_model.chain.model.keys() if "___BEGIN__" in key]):
#     print("{}:{}".format(k,i))

for i in range(5):
    print(str(i) + ":" + str(text_model.make_sentence(tries=10000)))

# Print three randomly-generated sentences of no more than 140 characters
# for i in range(3):
#     print(text_model.make_short_sentence(140))