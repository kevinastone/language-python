# SYNTAX TEST "source.python"


def right_hand_split(
# <- storage.type.function
#   ^^^^^^^^^^^^^^^^ entity.name.function
#                   ^ punctuation.definition.parameters.begin
    line: Line, py36: bool = False, omit: Collection[LeafID] = ()
#   ^^^^ variable.parameter.function
#       ^ punctuation.separator
#         ^^^^ storage.type
#             ^ punctuation.separator.parameters
#               ^^^^ variable.parameter.function
#                   ^ punctuation.separator
#                     ^^^^ storage.type
#                          ^ keyword.operator.assignment
#                            ^^^^^ constant
#                                 ^ punctuation.separator.parameters
#                                   ^^^^ variable.parameter.function
#                                       ^ punctuation.separator
#                                         ^^^^^^^^^^^^^^^^^^ storage.type
#                                                            ^ keyword.operator.assignment
) -> Iterator[Line]:
# ^^ keyword.operator.function-annotation
#    ^^^^^^^^^^^^^^ storage.type
#                  ^ punctuation.definition.function.begin
    pass


# Generics

Vector = List[float]
#      ^ keyword.operator.assignment
#        ^^^^^^^^^^^ meta.item-access
#            ^ punctuation.definition.arguments.begin
#             ^^^^^ meta.item-access.arguments
#                  ^ punctuation.definition.arguments.end


ConnectionOptions = Dict[str, str]
#                 ^ keyword.operator.assignment
#                   ^^^^^^^^^^^^^^ meta.item-access
#                       ^ punctuation.definition.arguments.begin
#                        ^^^^^^^^ meta.item-access.arguments
#                                ^ punctuation.definition.arguments.end


S = TypeVar('S')
# ^ keyword.operator.assignment
#   ^^^^^^^^^^^^ meta.function-call
#   ^^^^^^^ entity.name.function
#          ^ punctuation.definition.arguments.begin.bracket.round
#           ^^^ string.quoted.single
#              ^ punctuation.definition.arguments.end.bracket.round


Response = Union[Iterable[S], int]
#        ^ keyword.operator.assignment
#          ^^^^^^^^^^^^^^^^^^^^^^^ meta.item-access
#               ^ punctuation.definition.arguments.begin
#                ^^^^^^^^^^^^^^^^ meta.item-access.arguments
#                ^^^^^^^^^^^ meta.item-access
#                        ^ punctuation.definition.arguments.begin
#                         ^ meta.item-access.arguments
#                          ^ punctuation.definition.arguments.end
#                                ^ punctuation.definition.arguments.end


# New Types

UserId = NewType('UserId', int)
#      ^ keyword.operator.assignment
#        ^^^^^^^^^^^^^^^^^^^^^^ meta.function-call
#        ^^^^^^^ entity.name.function
#               ^ punctuation.definition.arguments.begin.bracket.round
#                ^^^^^^^^ string.quoted.single
#                             ^ punctuation.definition.arguments.end.bracket.round


# Generic Functions

T = TypeVar('T')


def first(l: Sequence[T]) -> T:
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.function
#   ^^^^^ entity.name.function
#         ^^^^^^^^^^^^^^ meta.function.parameters
#          ^ punctuation.separator
#            ^^^^^^^^^^^ storage.type
#                       ^ punctuation.definition.parameters.end.python
#                         ^^ keyword.operator.function-annotation
#                            ^ storage.type
#                             ^ punctuation.definition.function.begin
    return l[0]


def repeat(x: T, n: int) -> Sequence[T]:
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.function
#   ^^^^^^ entity.name.function
#          ^^^^^^^^^^^^ meta.function.parameters
#           ^ punctuation.separator
#              ^ punctuation.separator
#             ^     ^^^ storage.type
#                        ^^ keyword.operator.function-annotation
#                           ^^^^^^^^^^^ storage.type
#                                      ^ punctuation.definition.function.begin
    return [x] * n


T = TypeVar('T')
S = TypeVar('S', int, str)


def zip(x: List[T], y: List[S]) -> List[Tuple[T, S]]:
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.function
#   ^^^ entity.name.function
#       ^^^^^^^^^^^^^^^^^^^^^^ meta.function.parameters
#        ^           ^ punctuation.separator
#                 ^ punctuation.separator
#          ^^^^^^^     ^^^^^^^ storage.type
#                               ^^ keyword.operator.function-annotation
#                                  ^^^^^^^^^^^^^^^^^ storage.type
#                                              ^ punctuation.separator
#                                                   ^ punctuation.definition.function.begin
    ...


# Generic Classes

T = TypeVar('T')
S = TypeVar('S', int, str)


class StrangePair(Generic[T, S]):
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.class
#     ^^^^^^^^^^^ entity.name.type
#                 ^^^^^^^^^^^^^ meta.class.inheritance
#                        ^^^^^^ meta.item-access
#                        ^ punctuation.definition.arguments.begin
#                         ^^^^ meta.item-access.arguments
#                             ^ punctuation.definition.arguments.end
#                               ^ punctuation.section.class.begin
    pass
