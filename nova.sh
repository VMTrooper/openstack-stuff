#Deploy 5 instances

nova boot --num-instances 5 --image 7a9d43b5-8350-46b2-8c55-2292410ba283 \
--security-groups default --flavor m1.small \
--nic net-id=5d4abfaa-8fb2-4f50-bb68-668d0a1e1c7b CLI-Rocks
