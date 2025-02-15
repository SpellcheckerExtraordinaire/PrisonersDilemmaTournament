# # pylint: disable=C,W,R
# # type: ignore
# import random
#
# # Reminder: For the history array, "tell truth" = 0, "stay silent" = 1
#
import random

#
#
# def strategy(history, memory):
#     return 0, None
#
#
# # US = history[0]
# # THEM = history[1]
# # they_bad = len(list(filter(lambda x: x == 0, THEM)))
# # they_good = len(list(filter(lambda x: x == 1, THEM)))
# # if len(THEM) <= 1:  # Go defect first
# #     return 1, None
# # else:
# #     if they_bad > they_good:  # mostly fail? (as of right now)
# #         return 1, None  # Maybe it's tit for tat
# #     elif (
# #         they_good > they_bad
# #     ):  # Reminder: For the history array, "tell truth" = 0, "stay silent" = 1
# #         return 0, None  # Always good?
# #     else:
# #         if (  # Check if opponent seems random
# #             0.4
# #             < (
# #                 (they_bad if they_bad > 0 else 1)
# #                 / (they_good if they_good > 0 else 1)
# #             )
# #             < 0.6
# #         ):
# #             return 0, None
# #         # if len(history[1]) == 0:
# #         #     return 1, None
# #         return -history[1, -1], None
#
#
def strategy(history, memory):
    US = history[0]
    THEM = history[1]
    they_bad = len(list(filter(lambda x: x == 0, THEM)))
    they_good = len(list(filter(lambda x: x == 1, THEM)))
    if history.shape[1] == 0:  # We're on the first turn!
        return "stay silent", None
    else:
        if they_bad > they_good:  # mostly fail? (as of right now)
            return THEM[-1], None
        elif (
            they_good > they_bad
        ):  # Reminder: For the history array, "tell truth" = 0, "stay silent" = 1
            return 0, None  # Always good?
        else:
            if (  # Check if opponent seems random
                0.4
                < (
                    (they_bad if they_bad > 0 else 1)
                    / (they_good if they_good > 0 else 1)
                )
                < 0.6
            ) or they_good == they_bad:
                return 0, None

        # if they_bad > they_good:  # mostly fail? (as of right now)
        #     return THEM[-1], None
        # elif (
        #     they_good > they_bad
        # ):  # Reminder: For the history array, "tell truth" = 0, "stay silent" = 1
        #     return 0, None  # Always good?
        # else:
        #     if (  # Check if opponent seems random
        #         0.4
        #         < (
        #             (they_bad if they_bad > 0 else 1)
        #             / (they_good if they_good > 0 else 1)
        #         )
        #         < 0.6
        #     ):
        #         return 0, None
        #     if len(history[1]) == 0:
        #         return 1, None
        #     return history[1, 0], None


#
#
# # import random
# #
# #
# # def strategy(history, memory):
# #     if history.shape[1] <= 2:
# #         return 1, None
# #     else:
# #         if history[1, -1] == 0 and history[1, -2] == 0:
# #             return (random.randint(0, 1)), None
# #         elif history[1, -1] == 1 and history[1, -2] == 1:
# #             return 0, None
# #         else:
# #             return (random.randint(0, 1)), None
#
#
# def strategy(history, memory):
#     US = history[0]
#     THEM = history[1]
#     they_bad = len(list(filter(lambda x: x == 0, THEM)))
#     they_good = len(list(filter(lambda x: x == 1, THEM)))
#
#     if len(THEM) <= 1:  # Go coop first
#         return 1, None
#     else:
#         if they_bad > they_good:
#             return 1, None
#         else:
#             if they_good > they_bad:
#                 return 0, None
#             return THEM[-1], None
#
#
# # import random
# #
# #
# # def strategy(history, memory):
# #     if history.shape[1] <= 2:
# #         return 1, {}
# #     else:
# #         if history[1, -1] == 0 and history[1, -2] == 0:
# #             return (random.randint(0, 1)), {}
# #         elif history[1, -1] == 1 and history[1, -2] == 1:
# #             return 0, {}
# #         else:
# #             return (random.randint(0, 1)), {}
