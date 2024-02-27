from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class TaskAnonRateThrottle(AnonRateThrottle):
    rate = "10/minute"


class TaskUserRateThrottle(UserRateThrottle):
    rate = "100/minute"


class CategoryAnonRateThrottle(AnonRateThrottle):
    rate = "10/minute"


class CategoryUserRateThrottle(UserRateThrottle):
    rate = "100/minute"
