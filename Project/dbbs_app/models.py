from django.db import models


# Create your models here.
class QueryGroup(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = "query_groups"

    def __str__(self):
        return self.code


class Query(models.Model):
    code = models.CharField(max_length=20)
    query_text = models.CharField(max_length=500)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = "queries"
        ordering = ["id"]

    def __str__(self):
        return self.code


class QueryInGroup(models.Model):
    query_group = models.ForeignKey(
        "QueryGroup", on_delete=models.CASCADE, related_name="queries_in_groups"
    )
    query = models.ForeignKey(
        "Query", on_delete=models.CASCADE, related_name="queries_in_groups"
    )

    class Meta:
        db_table = "queries_in_groups"

    def __str__(self):
        return f"{self.query_group.code} {self.query.code}"


class ConnectionType(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = "connection_types"

    def __str__(self):
        return self.code


class Connection(models.Model):
    code = models.CharField(max_length=20)
    connection_type = models.ForeignKey(
        "ConnectionType", on_delete=models.PROTECT, related_name="connections"
    )
    description = models.CharField(max_length=200)
    host = models.CharField(max_length=100)
    port = models.CharField(max_length=10)
    database = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "connections"

    def __str__(self):
        return self.code


class Benchmark(models.Model):
    name = models.CharField(max_length=200)
    query_group = models.ForeignKey(
        "QueryGroup", on_delete=models.PROTECT, related_name="benchmarks"
    )
    connection = models.ForeignKey(
        "Connection", on_delete=models.PROTECT, related_name="benchmarks"
    )
    start_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "benchmarks"
        ordering = ["id"]

    def __str__(self):
        return self.name


class BenchmarkItem(models.Model):
    benchmark = models.ForeignKey(
        "Benchmark", on_delete=models.CASCADE, related_name="benchmark_items"
    )
    query = models.ForeignKey(
        "Query", on_delete=models.PROTECT, related_name="benchmark_items"
    )
    start_datetime = models.DateTimeField(auto_now_add=True)
    result = models.FloatField()

    class Meta:
        db_table = "benchmark_items"
        ordering = ["id"]

    def __str__(self):
        return str(self.pk)


class CompareBenchmarkItem(models.Model):
    query_code_1 = models.CharField(max_length=20)
    benchmark_name_1 = models.CharField(max_length=200)
    result_1 = models.FloatField()
    benchmark_name_2 = models.CharField(max_length=200)
    result_2 = models.FloatField()
    diff = models.CharField(max_length=20)

    class Meta:
        db_table = "compare_benchmarks_v"
        ordering = ["query_code_1"]

    def __str__(self):
        return self.query_code_1
