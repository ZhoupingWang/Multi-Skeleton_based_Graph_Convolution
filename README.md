# Multi-Skeleton based Graph convolution

## Dependencies

- Python >= 3.6
- PyTorch >= 1.2.0
- [NVIDIA Apex](https://github.com/NVIDIA/apex) (auto mixed precision training)
- PyYAML, tqdm, tensorboardX

#### NTU RGB+D 60

1. Request dataset here: http://rose1.ntu.edu.sg/Datasets/actionRecognition.asp

2. Download the skeleton-only datasets:
    - `nturgbd_skeletons_s001_to_s017.zip`  (NTU RGB+D 60)

3. Download missing skeletons lookup files [from the authors' GitHub repo](https://github.com/shahroudy/NTURGB-D#samples-with-missing-skeletons):
    - NTU RGB+D 60 Missing Skeletons:
      `wget https://raw.githubusercontent.com/shahroudy/NTURGB-D/master/Matlab/NTU_RGBD_samples_with_missing_skeletons.txt`

    - Remember to remove the first few lines of text in these files!

### Data Preprocessing

#### Directory Structure

Put downloaded data into the following directory structure:

```
- data/
  - nturgbd_raw/
    - nturgb+d_skeletons/     # from `nturgbd_skeletons_s001_to_s017.zip`
      ...
    - nturgb+d_skeletons120/  # from `nturgbd_skeletons_s018_to_s032.zip`
      ...
    - NTU_RGBD_samples_with_missing_skeletons.txt
    - NTU_RGBD120_samples_with_missing_skeletons.txt
```

#### Generating Data

1. NTU RGB+D
    - `cd data_gen`
    - `python3 ntu_gendata.py`
    - Time estimate is ~ 3hrs to generate NTU 120 on a single core (feel free to parallelize the code :))

3. Generate the bone data with:
    - `python gen_bone_data.py --dataset ntu`

4. Data description:
    - These files are raw data, without normalization and repetition, and only first person.
    - Action: 11-20
    - Camera view: [3]
    - Sample number: 2207/908
    - Data form: dict
      [[dict_keys(['joints']), ['C1', 'BL', ... 'RF', 'RB']],[dict_keys(['S017C003P007R002A012.skeleton']), data[frames-variable,joints-25,xyz-3]],............]


## Training & Testing

- The general training template command:
```
python main.py --config ./config/nturgbd-cross-subject/train_joint.yaml --work-dir ./work_dir/ntu/xsub/msg3d_joint
```

- The general testing template command:
```
python main.py --config ./config/nturgbd-cross-subject/test_joint.yaml --work-dir work_dir/ntu/xsub/msg3d_joint_val --weights work_dir/ntu/xsub/msg3d_joint/weights/weights-50-10400.pt
```

## Contact
Please email `wang.zhoup@northeastern.edu` or `zhu.shaot@northeastern.edu` for further questions
