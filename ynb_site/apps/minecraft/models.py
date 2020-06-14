from django.db import models


SERVER_TYPES = (
    ("survival", "survival"),
    ("creative", "creative"),
    ("Hardcore", "hardcore"),
    ("ultrahardcore", "ultra hard core")
)

class McServer(models.Model):
    """Model for a minecraft server."""
    name = models.CharField(max_length=200, unique=True)
    thumbnail = models.ImageField(upload_to="thmbnails", null=True, blank=True)
    founded_on = models.DateField()
    gamemode = models.CharField(max_length=200, choices=SERVER_TYPES, default="survival")
    description = models.TextField()
    features_description = models.TextField(null=True, blank=True)
    rules_description = models.TextField(null=True, blank=True)
    to_join_info = models.TextField(null=True, blank=True)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ServerFeature(models.Model):
    """Model for server features."""
    server = models.ForeignKey(McServer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    feature = models.TextField()

    def __str__(self):
        return f"{self.server.name} - {self.title}"


class ServerRule(models.Model):
    """Model for server rules."""
    server = models.ForeignKey(McServer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    rule = models.TextField()

    def __str__(self):
        return f"{self.server.name} - {self.title}"


class ServerEvent(models.Model):
    """Model for server events."""
    server = models.ForeignKey(McServer, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=200)
    event_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.server.name} - {self.event_title}"
