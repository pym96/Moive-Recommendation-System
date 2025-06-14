# 使用传统Recurrent Neural Networks完成中文文本分类任务

文本分类是NLP应用最广的任务之一，可以被应用到多个领域中，包括但不仅限于：情感分析、垃圾邮件识别、商品评价分类...

情感分析是一个自然语言处理中老生常谈的任务。情感分析的目的是为了找出说话者/作者在某些话题上，或者针对一个文本两极的观点的态度。这个态度或许是他或她的个人判断或是评估，也许是他当时的情感状态（就是说，作者在做出这个言论时的情绪状态），或是作者有意向的情感交流（就是作者想要读者所体验的情绪）。其可以用于数据挖掘、Web 挖掘、文本挖掘和信息检索方面得到了广泛的研究。可通过 [AI开放平台-情感倾向分析](http://ai.baidu.com/tech/nlp_apply/sentiment_classify) 线上体验。

<p align="center">
<img src="https://ai-studio-static-online.cdn.bcebos.com/febb8a1478e34258953e56611ddc76cd20b412fec89845b0a4a2e6b9f8aae774" hspace='10'/> <br />
</p>

本项目开源了一系列模型用于进行文本建模，用户可通过参数配置灵活使用。效果上，我们基于开源情感倾向分类数据集ChnSentiCorp对多个模型进行评测。

## paddlenlp.seq2vec

情感分析任务中关键技术是如何将文本表示成一个**携带语义的文本向量**。随着深度学习技术的快速发展，目前常用的文本表示技术有LSTM，GRU，RNN等方法。
PaddleNLP提供了一系列的文本表示技术，如`seq2vec`模块。

[`paddlenlp.seq2vec`](../../../paddlenlp/seq2vec) 模块作用为将输入的序列文本表征成一个语义向量。

<p align="center">
<img src="https://ai-studio-static-online.cdn.bcebos.com/bbf00931c7534ab48a5e7dff5fbc2ba3ff8d459940434628ad21e9195da5d4c6" width = "500" height = "200"  hspace='10'/> <br />
</p>


## 模型简介

本项目通过调用[seq2vec](../../../paddlenlp/seq2vec/)中内置的模型进行序列建模，完成句子的向量表示。包含最简单的词袋模型和一系列经典的RNN类模型。

`seq2vec`模块

* 功能是将序列Embedding Tensor（shape是(batch_size, num_token, emb_dim) ）转化成文本语义表征Enocded Texts Tensor（shape 是(batch_sie,encoding_size)）
* 提供了`BoWEncoder`，`CNNEncoder`，`GRUEncoder`，`LSTMEncoder`，`RNNEncoder`等模型
    - `LSTMEncoder` 是对输入序列Embedding Tensor进行LSTM运算，在运算结果上进行pooling或者取最后一个step的隐表示，得到文本语义表征Enocded Texts Tensor。
    


`seq2vec`提供了许多语义表征方法，那么这些方法在什么时候更加适合呢？

* `LSTMEnocder`采用LSTM方法，LSTM是RNN的一种变种。为了学到长期依赖关系，LSTM 中引入了门控机制来控制信息的累计速度，
    包括有选择地加入新的信息，并有选择地遗忘之前累计的信息。

<p align="center">
<img src="https://ai-studio-static-online.cdn.bcebos.com/a5af1d93c69f422d963e094397a2f6ce978c30a26ab6480ab70d688dd1929de0" width = "50%" height = "30%"  hspace='10'/> <br />
</p>


| 模型                                             | 模型介绍                                                     |
| ------------------------------------------------ | ------------------------------------------------------------ |
| BOW（Bag Of Words）                              | 非序列模型，将句子表示为其所包含词的向量的加和               |
| RNN (Recurrent Neural Network)                   | 序列模型，能够有效地处理序列信息                             |
| GRU（Gated Recurrent Unit）                      | 序列模型，能够较好地解决序列文本中长距离依赖的问题           |
| LSTM（Long Short Term Memory）                   | 序列模型，能够较好地解决序列文本中长距离依赖的问题           |
| Bi-LSTM（Bidirectional Long Short Term Memory）  | 序列模型，采用双向LSTM结构，更好地捕获句子中的语义特征       |
| Bi-GRU（Bidirectional Gated Recurrent Unit）     | 序列模型，采用双向GRU结构，更好地捕获句子中的语义特征        |
| Bi-RNN（Bidirectional Recurrent Neural Network） | 序列模型，采用双向RNN结构，更好地捕获句子中的语义特征        |
| Bi-LSTM Attention                                | 序列模型，在双向LSTM结构之上加入Attention机制，结合上下文更好地表征句子语义特征 |
| TextCNN                                          | 序列模型，使用多种卷积核大小，提取局部区域地特征             |


| 模型  | dev acc | test acc |
| ---- | ------- | -------- |
| BoW  |  0.8970 | 0.8908   |
| Bi-LSTM  | 0.9098  | 0.8983  |
| Bi-GRU  | 0.9014  | 0.8785  |
| Bi-RNN  | 0.8649  |  0.8504 |
| Bi-LSTM Attention |  0.8992 |  0.8856 |
| TextCNN  | 0.9102  | 0.9107 |


<p align="center">
<img src="https://ai-studio-static-online.cdn.bcebos.com/ecf309c20e5347399c55f1e067821daa088842fa46ad49be90de4933753cd3cf" width = "600" height = "200"  hspace='10'/> <br />
</p>



## 快速开始

### 代码结构说明

以下是本项目主要代码结构及说明：

```text

```

### 数据准备

#### 使用PaddleNLP内置数据集

### 安装依赖
```
python 3.7+
paddlenlp==2.2.4
paddlepaddle==2.2.2
jieba
```

```python
from paddlenlp.datasets import load_dataset

train_ds, dev_ds, test_ds = load_dataset("chnsenticorp", splits=["train", "dev", "test"])
```


### 模型训练

我们以中文情感分类公开数据集ChnSentiCorp为示例数据集，可以运行下面的命令，在训练集（train.tsv）上进行模型训练，并在开发集（dev.tsv）验证

CPU 启动：

```shell
python train.py --vocab_path='./vocab.json' --device=cpu --network=rnn --lr=5e-4 --batch_size=64 --epochs=10 --save_dir='./checkpoints2'
```

### 模型预测

启动预测：

使用方法如下：

```shell
data = [
        '非常不错，服务很好，位于市中心区，交通方便，不过价格也高！',
        '怀着十分激动的心情放映，可是看着看着发现，在放映完毕后，出现一集米老鼠的动画片',
        '作为老的四星酒店，房间依然很整洁，相当不错。机场接机服务很好，可以在车上办理入住手续，节省时间。',
        '你们把苏州当乌克兰是不是，领了纳税人的工资就合伙打击报复纳税人吗？这事不说清楚我直接写挂号信给省委书记和市委书记'
    ]
model = LSTMSentiment(model_path='./checkpoints/final.pdparams',vocab_path='./vocab.json')
results = model.predict(data)
for i in results:
    print(i)
```

将待预测数据分词完毕后，如以下示例：

```text
非常不错，服务很好，位于市中心区，交通方便，不过价格也高！
怀着十分激动的心情放映，可是看着看着发现，在放映完毕后，出现一集米老鼠的动画片
作为老的四星酒店，房间依然很整洁，相当不错。机场接机服务很好，可以在车上办理入住手续，节省时间。
```

处理成模型所需的`Tensor`，如可以直接调用`preprocess_prediction_data`函数既可处理完毕。之后传入`predict`函数即可输出预测结果。

如

```text
Data: 非常不错，服务很好，位于市中心区，交通方便，不过价格也高！      Label: negative
Data: 怀着十分激动的心情放映，可是看着看着发现，在放映完毕后，出现一集米老鼠的动画片      Label: negative
Data: 作为老的四星酒店，房间依然很整洁，相当不错。机场接机服务很好，可以在车上办理入住手续，节省时间。      Label: positive
```

## Reference

关于LSTM、GRU、CNN更多信息参考：

- https://canvas.stanford.edu/files/1090785/download
- https://colah.github.io/posts/2015-08-Understanding-LSTMs/
- https://arxiv.org/abs/1412.3555
- https://arxiv.org/pdf/1506.00019
- https://arxiv.org/abs/1404.2188
