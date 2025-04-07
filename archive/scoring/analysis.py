import pandas as pd

file_path = "output.json"

df = pd.read_json(file_path)
# df = df["input.title"]#, "output.total_score"]
inputDf = df["input"].to_frame()
outputDf = df["output"].to_frame()

print(inputDf.head())

titles = df["input"].apply(lambda x: x["title"])
shareLink = df["input"].apply(lambda x: x["share_link"])
scores = df["output"].apply(lambda x: x["total_score"])

print(titles)
print(scores)


df = pd.DataFrame({"title": titles, "Scores": scores, "Share Link": shareLink})
df_sorted = df.sort_values("Scores", ascending=False)
print(df)
df_sorted.to_json("sorted.json", orient="records")
