import sympy
import math

def compute_radical(n):
    """计算数字的根基 (Radical)"""
    if n <= 1: return 1
    factors = sympy.factorint(n)
    rad = 1
    for p in factors.keys(): rad *= p
    return rad

def weapon_A_residue_sieve(n, p):
    """武器 A：模 p 对称性扫描"""
    print(f"\n[⚔️ 武器 A 激活] 完备剩余系对称性扫描")
    print(f"[*] 标尺 Q(n) = 2n-1 = {p} (已确认为素数)")
    
    start_val = (n-1)**2
    end_val = n**2
    inner_numbers = list(range(start_val + 1, end_val))
    
    print(f"[*] 区间内部数字数量: {len(inner_numbers)} (恰好等于 p-1)")
    
    # 寻找那个隐藏的 p 的倍数
    multiple_of_p = None
    for x in inner_numbers:
        if x % p == 0:
            multiple_of_p = x
            break
            
    print(f"[*] 发现绝对锚点：区间内唯一的 {p} 的倍数是 {multiple_of_p}")
    
    # 测算二次剩余自旋 (Legendre Symbol)
    spins = []
    for x in inner_numbers:
        if x == multiple_of_p:
            continue
        # 计算勒让德符号 (x/p)
        spin = sympy.jacobi_symbol(x, p)
        spins.append(spin)
        
    positive_spin = spins.count(1)
    negative_spin = spins.count(-1)
    
    print(f"[*] 代数自旋状态: 正自旋(+1)={positive_spin}个, 负自旋(-1)={negative_spin}个")
    if positive_spin == negative_spin:
        print("[*] 结论: 大自然维持了绝对的代数对称性！")

def weapon_B_wronskian_volume(n):
    """武器 B：连续合数序列的根基体积测算"""
    print(f"\n[⚔️ 武器 B 激活] 离散朗斯基体积/ABC 测算")
    
    start_val = (n-1)**2
    end_val = n**2
    
    # 找到该区间内最长的一段“素数真空”（连续合数序列）
    max_gap_seq = []
    current_gap = []
    
    for x in range(start_val, end_val + 1):
        if not sympy.isprime(x):
            current_gap.append(x)
        else:
            if len(current_gap) > len(max_gap_seq):
                max_gap_seq = current_gap
            current_gap = []
    if len(current_gap) > len(max_gap_seq):
        max_gap_seq = current_gap
        
    gap_len = len(max_gap_seq)
    if gap_len == 0:
        print("[*] 区间内全是素数，无法测算合数体积。")
        return
        
    print(f"[*] 锁定最长素数真空地带: 长度 {gap_len} (从 {max_gap_seq[0]} 到 {max_gap_seq[-1]})")
    
    # 计算这段真空序列的总根基体积
    total_product = 1
    for x in max_gap_seq:
        total_product *= x
        
    total_radical = compute_radical(total_product)
    
    # 计算压缩率
    # 理论最大根基体积 = total_product
    compression_ratio = math.log(total_product) / math.log(total_radical) if total_radical > 1 else 1.0
    
    print(f"[*] 真空序列的理论总体积 (log): {math.log(total_product):.2f}")
    print(f"[*] 真实的离散朗斯基根基 (log): {math.log(total_radical):.2f}")
    print(f"[*] 序列整体 ABC 压缩比率: {compression_ratio:.4f}")

def main(n):
    print("==================================================")
    print(f"🚀 泰坦降维打击测试 (目标区间: n={n})")
    print("==================================================")
    
    p = 2*n - 1
    if not sympy.isprime(p):
        print(f"[!] 警告：标尺 2n-1 = {p} 不是素数，武器 A 的对称性将衰减。建议更换 n 值。")
    else:
        weapon_A_residue_sieve(n, p)
        
    weapon_B_wronskian_volume(n)

if __name__ == '__main__':
    # 我们先在 n=20 这个微观尺度上，找一个标尺为素数的区间
    # 当 n=20 时，2n-1 = 39 (合数，不佳)
    # 当 n=21 时，2n-1 = 41 (素数，完美靶场！)
    # 舰长，您可以将 21 改为更大的数字（只要 2n-1 是素数）
    main(21)