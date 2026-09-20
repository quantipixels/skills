def defer_notification(notification, until):
    # Notification scheduling is independent of collection eligibility.
    notification["deferred_until"] = until
