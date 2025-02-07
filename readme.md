## Порівняння алгоритмів сортування

Емпіричні дані показують час виконання (в секундах) алгоритмів сортування на наборах даних різного розміру:

Dataset size   : 10;
Merge Sort     : 0.000011;
Insertion Sort : 0.000005;
Timsort        : 0.000001;

Dataset size   : 100;
Merge Sort     : 0.000092;
Insertion Sort : 0.000126;
Timsort        : 0.000004;

Dataset size   : 1000;
Merge Sort     : 0.001114;
Insertion Sort : 0.014117;
Timsort        : 0.000065;

Dataset size   : 10000;
Merge Sort     : 0.014984;
Insertion Sort : 1.355066;
Timsort        : 0.000726;


### Основні спостереження

- **Merge Sort:** Показує стабільний і відносно низький час виконання, хоча і не такий швидкий, як Timsort. Але на дуже малих списках програє навіть Insertion Sort.
- **Insertion Sort:** Добре працює на дуже малих наборах даних. Однак його продуктивність швидко погіршується на великих наборах даних, що робить його непрактичним для більшості реальних застосувань у порівнянні з іншими алгоритмами.
- **Timsort:** Послідовно перевершує сортування злиттям і сортування вставками для всіх розмірів наборів даних. Він використовує переваги обох алгоритмів, поєднуючи ефективне злиття від сортування злиттям і швидку роботу сортування вставкою на частково впорядкованих наборах даних. Також, припускаю, що він є таким швидким частково через те, що "під капотом" імплементований на С.