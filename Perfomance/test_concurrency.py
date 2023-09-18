import concurrency

#we are going to benchmark concurrency


# Benchmark and test

def test_concurrency(benchmark):
    assert concurrency.network_request(5) == {"success": True, "result": 25}
    benchmark(concurrency.network_request, 5)