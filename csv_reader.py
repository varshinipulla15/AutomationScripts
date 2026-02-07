import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(BASE_DIR, "data.csv")

#path = "C:/Users/VARSHINI/Projects/Phython/data.csv"

def csv_reader(file_path):
    try:
        with open(file_path, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            count = 0
            total_score = 0
            results = {}

            for row in reader:
                name = row["name"]
                score = float(row["score"])
                results[name] = score
                count += 1
                total_score += score

            average_score = total_score / count if count else 0

            for name, score in results.items():
                print (f"{name} : {score}")
            print (f"Average Score : {average_score:.2f}")

    except FileNotFoundError:
        print (f"File is not found in this path {file_path}")
        return {}, 0
    except Exception as e:
        print (f"Exception : {e}")
        return {}, 0
    
if __name__ == "__main__":
    csv_reader(csv_file)