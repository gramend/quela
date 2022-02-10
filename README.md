# Quela

Платформа для анализа изученной информации.

## Проработка омдели данных:


![](https://www.plantuml.com/plantuml/png/hLJ1Rjim3BtxAxGFAB0Do4MdTedN672RDN5s2Gf3Ynb7WosxajmjAFhlasGpjk8am8QTBF4zaeyKwLkbcTHDMGGVz1vA87N1k0W249hh0rahaEGj8AGn1y5Ae6IwP_8hXoBRV9fyV3RGZakbqmjWmIvZK39UK1BQZmTmbHfPknqbNwgg02OSsW9ig_ahZ92CQKX_Lbn0HidCN19U0eAvh9fQKN9llvldu1tBSmPNNoUHxNs9jcn5NHisziwKuhd9aMwPXhoI79JrSkU3YuoXqOZHlGPydanij0pKLl9QyqfGai1lZO8lH2VafG5bwSR-r1rzNLwfhPocF7AJGmtAALfy2n_JftMuIgB5exbFvuje6gw6feTrd4JfAK2iyt8MBZtgNJATzuRJj36yGj7cZQFxUPB6tsFh5SrcSTXTvWPmnxw5wEuSjMcFtwINGL7KBn5Hp4rFf5nhCHFgbtlqEtTmjgq4GybIfiV3rTJP1Gp7h8laoa1PlQ9kojeXErke15KLZUMYgENHOiLLPMaIsJhQq_-JtEUvEiRie5OrC-eYOHe9BNgsbHWVfPgmI4FMt_K3k_ZF5O_7xO49bdVFLJS_2gxsPsDg9dFGgISMdtVyK3QH9L7QhYXvlxbvQzUKKXj31JY6bFhhx7F7lw2X9mheVB0cIWVitjXstd4xmNs40MsuQSHGlLtpULhXaWs8k7MOmfPhOTSqDE8OMp4u7gWmmBllUl9YbEAJN2LXDKE1HnKuMmuUF-8jYAmfYpy0)

Исходник:
```
@startuml
!theme plain

entity User {
  username: CharField[150]
  first_name: CharField[150]
  last_name: CharField[150]
  email: EmailField[150]
  is_staff: BooleanField
  is_active: BooleanField
  date_joined: DateTimeField
  groups: Group[]
}
entity Group {
  name: CahrField[150]
  users: User[]
  assigned_categories: Category[]
}

entity Category {
  name: CharField[255]
  description: TextField
  categories: Category[]
  questions: Question[]
  assigned_groups: Group
}

enum QuestionTypes {
  OPEN_QUESTION
  CHOICES_QUESTION
  MULTI_CHOICES_QUESTION
  ORDER_QUESTION
  MATCH_QUESTION
}

enum QuestionLevels {
  LIGHT_LVL
  MIDDLE_LVL
  HIGH_LVL
}

entity Question {
  text: TextField
  questionType: QuestionTypes
  questionLevel: QuestionLevels
  categories: Category[]
  answers: Answer[]
  created_at: DateTimeField
  updated_at: DateTimeField
}
entity Answer {
  question: Question
  user: User
  text: TextField
  resolution: AnswerResolution
  comments: Comment[]
  created_at: DateTimeField
  updated_at: DateTimeField
}
entity AnswerResolution {
  name: CharField[255]
  daysSpan: IntegerField
  answers: Answer[]
}
entity Comment {
  answer: Answer
  user: User
  text: TextField
  resolution: Question
  created_at: DateTimeField
  updated_at: DateTimeField
}

entity QuestionManager {
  publish_at: DateTimeField
  target_user: User
  question: AnswerResolution
}

User::groups }--{ Group::users
Category::assigned_groups }--{ Group::assigned_categories
Category::questions }--{ Question::categories
Question::answers }-- Answer::question
Question::questionType -- QuestionTypes
Question::quetsionLevel -- QuestionLevels
Answer::user -- User
Answer::comments }-- Comment::answer
Comment::user -- User
QuestionManager::target_user -- User
QuestionManager::question -- Question
Answer::resolution -- AnswerResolution
@enduml
```
