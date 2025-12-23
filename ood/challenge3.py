class Question:
    def __init__(self, text, topic, category):
        self.text = text
        self.topic = topic
        self.category = category

class MCQuestion(Question): # Inheritance
    pass

class ParaQuestion(Question): # Inheritance
    pass

class Exam:
    def __init__(self):
        self.questions = [] # List to store Question objects

    def add_question(self, question):
        self.questions.append(question)

    # Query 1: Total number of questions.Calculates the length of the list
    def get_total_count(self):
        return len(self.questions)

    # Query 2: List all questions belonging to a topic
    def get_by_topic(self, topic_name):
        return [q.text for q in self.questions if q.topic == topic_name]

    # Query 3: List by topic and category
    def get_by_topic_and_category(self, topic_name, cat_name):
        return [q.text for q in self.questions 
                if q.topic == topic_name and q.category == cat_name]

# Testing the Logic
if __name__ == "__main__":
    exam = Exam()
    exam.add_question(MCQuestion("What is Python?", "Programming", "Easy"))
    exam.add_question(ParaQuestion("Explain Classes.", "OO Design", "Medium"))

    print(f"Total Questions: {exam.get_total_count()}")
    print(f"Programming Questions: {exam.get_by_topic('Programming')}")