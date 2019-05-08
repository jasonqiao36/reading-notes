# dict的特点

- 键必须是可散列的
- 内存开销大
- 查询快
- 键的次序取决于添加顺序
- 往字典里添加新键可能改变已有键的顺序

# 小结
字典算的上是Python的基石。除了基本的dict外，标准库还提供了特殊的映射类型, 比如defaultdict, OrderedDict, ChainMap
和Counter. 这些映射类型都属于collections模块，这个模块还提供了易于扩展的UserDict类.

大多数的映射类型都提供了两个很强大的方法: setdefault和update.

在映射类型的Api中，有个很好的方法，__missing__，当找不到键时，可以通过这个方法自定义会发生什么.

collections.abc提供了Mapping和MutableMapping这两个抽象基类，利用他们，我们可以进行类型查询和引用.

dict和set背后的散列表效率很高.
