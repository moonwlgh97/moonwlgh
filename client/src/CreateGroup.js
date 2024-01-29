import { useState } from "react";

import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalBody,
    ModalCloseButton,
    Button,
    useDisclosure,
    Image,
    VStack,
    Text,
    FormControl,
    Input,
} from "@chakra-ui/react";

const CreateGroup = () => {
    const [groupData, setGroupData] = useState([]);
    const [groupName, setGroupName] = useState(""); // 그룹 이름 상태 추가
    const { isOpen, onOpen, onClose } = useDisclosure();

    const onGroupCreate = () => {
        const newGroupData = {
            groupName,
        };
        setGroupData([...groupData, newGroupData]); // 그룹 데이터 배열에 추가
        onClose();
    };

    const handleGroupNameChange = (e) => {
        setGroupName(e.target.value); // 입력된 그룹 이름 설정
    };

    return (
        <div className="CreateGroup">
            <img src="/logo.png" alt="logoImg" />
            {groupData.length < 1 ? (
                <>
                    <p>
                        소속된 그룹이 없습니다! <br />
                        그룹을 생성하고 멤버를 초대해 주세요!
                    </p>

                    <div>
                        <button onClick={onOpen}>+</button>
                    </div>
                </>
            ) : (
                <>
                    <p>그룹 선택하기</p>
                    <p>{groupData.groupName}</p>
                </>
            )}

            <Modal isOpen={isOpen} onClose={onClose} isCentered>
                <ModalOverlay />
                <ModalContent width="md" p={5} mx="auto" my="auto">
                    <ModalHeader> </ModalHeader>
                    <ModalCloseButton />
                    <ModalBody>
                        <Image
                            src="/logo.png"
                            alt="Logo"
                            mx="auto"
                            my={4}
                            boxSize="70%"
                        />
                        <VStack spacing={4}>
                            <Text mb={3}>그룹 생성하기</Text>

                            <FormControl>
                                <Input
                                    mb={3}
                                    placeholder="그룹이름"
                                    value={groupName}
                                    onChange={handleGroupNameChange}
                                />
                            </FormControl>

                            <Button
                                colorScheme="yellow"
                                size="md"
                                w="full"
                                onClick={onGroupCreate}
                            >
                                그룹 만들기
                            </Button>

                            {/* 다른 소셜 로그인 버튼들 추가 */}
                        </VStack>
                    </ModalBody>
                </ModalContent>
            </Modal>
        </div>
    );
};

export default CreateGroup;
