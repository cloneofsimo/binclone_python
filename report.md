| Region Length | WINDOW SIZE | SBSIZE | ACCURACY |
| ------------- | ----------- | ------ | -------- |
| 40            | 40          | 17     | 50%      |
| 80            | 40          | 22     | 50%      |
|               |             |        |          |

after fix,

| Region Length | WINDOW SIZE | SBSIZE | ACCURACY |
| ------------- | ----------- | ------ | -------- |
| 40            | 40          | 17     | 100%     |
| 80            | 40          | 22     | 100%     |
|               |             |        |          |

So only interest is precision : how many other document would they give?


| Region Length | WINDOW SIZE | SBSIZE | Average Precision |
| ------------- | ----------- | ------ | ----------------- |
| 80            | 40          | 17     | 14%               |
| 80            | 40          | 22     | 36.9%             |
| 80            | 40          | 24     | 58.3%             |

Does less feature give smaller precision?

Smaller feature means smaller SBSize. But, they are more significant.

| Region Length | WINDOW SIZE | SBSIZE | Average Precision |
| ------------- | ----------- | ------ | ----------------- |
| 40            | 40          | 17     | 36%               |
| 40            | 40          | 14     | 20%               |

