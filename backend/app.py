def check_plagiarism(text1, text2):
    words1 = set(text1.split())
    words2 = set(text2.split())
    common = words1.intersection(words2)
    similarity = (len(common) / len(words1)) * 100
    return round(similarity, 2)

# Sample test
if __name__ == "__main__":
    t1 = "this is a sample text"
    t2 = "this text is a sample"
    print("Similarity:", check_plagiarism(t1, t2), "%")
