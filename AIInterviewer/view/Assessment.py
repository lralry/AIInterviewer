class Assessment:
    def __init__(self, intro_rate):
        self.__full_score = 100
        self.__intro_rate = intro_rate

    # 获得总分
    def get_score(self):
        score = self.__get_intro_score() + self.__get_question_score()
        return score

    # 自我介绍的分数
    def __get_intro_score(self):
        # 给出各个维度的比例
        time_rate = 0.2
        attitude_rate = 0.4
        content_rate = 1 - time_rate - attitude_rate

        intro = (time_rate * self.__intro_time_score() +
                 attitude_rate * self.__intro_att_score() +
                 content_rate * self.__intro_cont_score()) * self.__intro_rate

        print("自我介绍得分: " + str(intro))
        return intro

    # 回答问题的得分
    def __get_question_score(self):
        # TODO:gpt得分接口,4题
        score_queue = [100, 100, 100, 100]

        # 每一题权重相等
        ques = sum(score_queue) / len(score_queue) * (1 - self.__intro_rate)
        print("回答问题得分: " + str(ques))
        return ques

    # 自我介绍时间得分，满分取self.__fullscore
    def __intro_time_score(self):
        # TODO:计时器接口
        time = 43

        # 没到1分钟，按比例给分
        if time < 60:
            return self.__full_score * (time / 60)
        # 到了1分钟，满分
        else:
            return self.__full_score

    # 自我介绍态度得分
    # 情感识别接口
    def __intro_att_score(self):
        # TODO:情感识别
        return 100

    # 自我介绍内容得分
    # TODO:如何得分？
    def __intro_cont_score(self):
        return 100
