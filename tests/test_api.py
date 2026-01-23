import requests
import time

print("🧪 Starting API tests...")
print("=" * 50)


def test_price_endpoints():
    print("   Testing price endpoints...")

    print("   Waiting 5 seconds for data...")
    time.sleep(5)

    endpoints = [
        ("/api/v1/prices?ticker=BTC_USD", "BTC prices"),
        ("/api/v1/prices?ticker=ETH_USD", "ETH prices"),
        ("/api/v1/prices/latest?ticker=BTC_USD", "Latest BTC"),
        ("/api/v1/prices/latest?ticker=ETH_USD", "Latest ETH"),
    ]

    all_ok = True
    for url, name in endpoints:
        try:
            resp = requests.get(f"http://localhost:8000{url}", timeout=10)

            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, list):
                    print(f"   ✅ {name}: {len(data)} records")
                else:
                    print(f"   ✅ {name}: ${data.get('price', 0):.2f}")
            elif resp.status_code == 404:
                print(f"   ⚠️  {name}: No data yet (normal at start)")
            else:
                print(f"   ❌ {name}: Error {resp.status_code}")
                all_ok = False

        except Exception as e:
            print(f"   ❌ {name}: {e}")
            all_ok = False

    return all_ok


tests = [test_price_endpoints]

print("\n🔧 Running tests...")
results = []

for test in tests:
    results.append(test())
    print()

# Итоги
print("=" * 50)
print("📊 Test Results:")
passed = sum(results)
total = len(results)

for i, (test, result) in enumerate(zip(tests, results), 1):
    status = "✅ PASS" if result else "❌ FAIL"
    print(f"{status} Test {i}: {test.__name__}")

print(f"\n🎯 Total: {passed}/{total} passed")

if passed == total:
    print("✨ All tests passed!")
else:
    print("💥 Some tests failed")