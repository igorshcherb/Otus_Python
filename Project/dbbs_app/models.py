from django.db import models


# Create your models here.
class QueryGroup(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.code


class Query(models.Model):
    code = models.CharField(max_length=20)
    query_text = models.CharField(max_length=500)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = "queries"

    def __str__(self):
        return self.code


class QueryInGroup(models.Model):
    group_code = models.ForeignKey(
        "QueryGroup", on_delete=models.CASCADE, related_name="queries_in_groups"
    )
    query_code = models.ForeignKey(
        "Query", on_delete=models.CASCADE, related_name="queries_in_groups"
    )

    def __str__(self):
        return f"{self.group_code} {self.query_code}"


class ConnectionType(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.code


class Connection(models.Model):
    code = models.CharField(max_length=20)
    type_code = models.ForeignKey(
        "ConnectionType", on_delete=models.CASCADE, related_name="connections"
    )
    description = models.CharField(max_length=200)
    host = models.CharField(max_length=100)
    port = models.CharField(max_length=10)
    database = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class Benchmark(models.Model):
    name = models.CharField(max_length=200)
    query_group_code = models.ForeignKey(
        "QueryGroup", on_delete=models.CASCADE, related_name="benchmarks"
    )
    start_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BenchmarkItem(models.Model):
    benchmark_id = models.ForeignKey(
        "Benchmark", on_delete=models.CASCADE, related_name="benchmark_items"
    )
    query_code = models.ForeignKey(
        "Query", on_delete=models.CASCADE, related_name="benchmark_items"
    )
    start_datetime = models.DateTimeField(auto_now_add=True)
    result = models.FloatField()

    def __str__(self):
        return self.pk
