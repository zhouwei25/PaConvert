# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

from apibase import APIBase

obj = APIBase("torch.take_along_dim")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1, 2, 3], [3, 4, 6]])
        idx = torch.tensor([[0]])
        result = torch.take_along_dim(x, idx, 1)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1, 2, 3], [3, 4, 6]])
        idx = torch.tensor([[0]])
        result = torch.take_along_dim(input=x, indices=idx, dim=0)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1, 2, 3], [3, 4, 6]], dtype=torch.float32)
        idx = torch.tensor([[0]])
        out = torch.tensor([])
        result = torch.take_along_dim(x, indices=idx, dim=1, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1, 2, 3], [3, 4, 6]], dtype=torch.float32)
        idx = torch.tensor([[0]])
        out = torch.tensor([])
        result = torch.take_along_dim(input=x, indices=idx, dim=1, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[1, 2, 3], [3, 4, 6]], dtype=torch.float32)
        idx = torch.tensor([[0]])
        out = torch.tensor([])
        result = torch.take_along_dim(dim=1, indices=idx, input=x, out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])
