# 大模型回答偏好预测

同一个问题有两份回答，用户会选哪一份？我在 Gemma-2 和 Llama-3 的公开双模型方案上改了长对话的截断方式。只保留开头时，排在后面的回答可能被切掉。改成保留头尾后，模型还能看到最后的回答片段。

默认对话预算是 **4,096 个 token**。超限时保留前 2,896 个和最后 1,200 个，短对话保留原样。完整推理仍沿用原方案的 A/B 换序后合并结果。 [我的完整 Kaggle 笔记本](https://www.kaggle.com/code/gloriachen0816/llmclf-headtail-r6) · [snaykey 的原方案](https://www.kaggle.com/code/snaykey/gemma-2-llama-3-preference-ensemble-on-2xt4)

| 我的 Kaggle 提交 | 公开榜对数损失（越低越好） |
| --- | ---: |
| 只保留开头 | 0.82756 |
| 保留开头和结尾 | 0.82728 |

另一个公开方案的复现得到 0.82685，对应不同的推理流程。 [复现笔记本](https://www.kaggle.com/code/gloriachen0816/llmclf-ander-r7)

## 试一下截断逻辑

[`head_tail.py`](head_tail.py) 提取了我加的 token 处理逻辑，只用 Python 3。运行下面的示例，可以看到旧方法切掉的末尾如何保留下来：

```bash
python head_tail.py
```

也可将 `keep_head_and_tail(token_ids, max_tokens=4096)` 用在已有分词流程里。要重跑模型推理，可打开上面的 Kaggle 笔记本，使用其中的双 T4 环境和公开模型权重。
